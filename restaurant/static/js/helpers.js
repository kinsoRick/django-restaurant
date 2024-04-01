// DOM manipulation helper functions
const getElement = (id) => document.getElementById(id);

// Cookie-related helper functions //
const debounce = (callback, wait) => {
  let timeoutId = null;
  return (...args) => {
    window.clearTimeout(timeoutId);
    timeoutId = window.setTimeout(() => {
      callback(...args);
    }, wait);
  };
};

const getCookie = (cname) => {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return false;
};

const refreshLikedNotification = () => {
  const likedPositionsNotification = getElement("likedPositions");
  const rawData = getCookieOrFalse("likedPositions");
  const likedPositions = JSON.parse(rawData) || [];

  likedPositionsNotification.textContent = likedPositions.length;

  if (likedPositions.length > 0) {
    likedPositionsNotification.classList.remove("d-none");
  } else {
    likedPositionsNotification.classList.add("d-none");
  }
};

const setCookie = (cname, cvalue, exdays) => {
  const d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  let expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + JSON.stringify(cvalue) + ";" + expires + ";path=/";
};

const getCookieOrFalse = (cname) => {
  const cookieRaw = getCookie(cname);
  if (cookieRaw !== "") return cookieRaw;
  return false;
};

// Like-related functions //
const toggleLike = (event) => {
  const positionId = parseInt(event.dataset.positionId);
  const rawData = getCookie(LIKED_POSITIONS) || '[]';

  let likedPositions = JSON.parse(rawData) || [];

  if (likedPositions.includes(positionId)) {
    likedPositions = likedPositions.filter(position => position !== positionId);
  } else {
    likedPositions.push(positionId);
  }

  setCookie(LIKED_POSITIONS, likedPositions, 365);

  const isFavorite = likedPositions.includes(positionId);

  const newLike = document.createElement("span");
  newLike.classList.add("material-icons");
  newLike.textContent = isFavorite ? "favorite" : "favorite_border";
  if (isFavorite) newLike.classList.add("active");

  // Update material icon
  event.children[0].remove();
  event.appendChild(newLike);

  return refreshLikedNotification();
};

// Builder cards
function createCard(positionData) {
  const createAnElementWithClasses = (elementName, classes) => {
    const element = document.createElement(elementName);
    element.classList.add(...classes.split(" "));
    return element;
  };

  const createCardElement = (element, textContent = "") => {
    const cardElement = createAnElementWithClasses(element[0], element[1]);

    if (textContent) {
      cardElement.textContent = textContent;
    }

    return cardElement;
  };

  const elements = {
    row: createCardElement(["div", "row g-3"]),
    cardFooter: createCardElement(["div", "card-footer"]),
    cardBody: createCardElement(["div", "card-body px-md-0"]),
    container: createCardElement(["div", "card mb-3 position"]),
    positionImageContainer: createCardElement(["div", "col-4"]),
    positionHeader: createCardElement(["div", "position-header"]),
    textContainer: createCardElement(["div", "col-8 position-text"]),
    btnRemove: createCardElement(["button", "remove-btn"]),
    positionAdditionals: createCardElement(["div", "position-additionals"]),
    positionImage: createCardElement(["img", "img-fluid rounded-start thumbnail"]),
    positionTitle: createCardElement(["h5", "card-title"], positionData.name),
    positionCurrency: createCardElement(["small", "position-currency"], " руб"),
    description: createCardElement(["p", "card-text"], positionData.description),
    positionPrice: createCardElement(["span", "position-price"], positionData.price),
    cookingTime: createCardElement(["span", "text-dark time ml-auto"], `${positionData.cooking_time} минут`),
    weight: createCardElement(["span", "bg-weight badge text-dark position-weight"], `${positionData.weight}`),
  };

  elements.positionImage.src = positionData.image;
  elements.positionImage.dataset.positionId = `#position-${positionData.id}`;
  elements.positionImage.alt = "Картинка позиции";

  const removeBtnSpan = createCardElement(["span", "material-icons"], null, "close");

  elements.btnRemove.appendChild(removeBtnSpan);
  elements.btnRemove.dataset.positionId = positionData.id;
  elements.btnRemove.addEventListener("click", () => removeLike(elements.btnRemove));

  if (positionData.weight > 0) {
    elements.positionAdditionals.appendChild(elements.weight);
  }

  if (positionData.cooking_time > 0) {
    elements.positionAdditionals.appendChild(elements.cookingTime);
  }

  elements.cardBody.appendChild(elements.positionHeader);
  elements.cardBody.appendChild(elements.positionAdditionals);
  elements.cardBody.appendChild(elements.description);

  elements.positionHeader.appendChild(elements.positionTitle);
  elements.positionHeader.appendChild(elements.btnRemove);

  elements.cardFooter.appendChild(elements.positionPrice);
  elements.cardFooter.appendChild(elements.positionCurrency);

  elements.positionImageContainer.appendChild(elements.positionImage);

  elements.row.appendChild(elements.positionImageContainer);

  elements.row.appendChild(elements.textContainer);
  elements.row.appendChild(elements.cardFooter);

  elements.textContainer.appendChild(elements.cardBody);
  elements.container.appendChild(elements.row);

  return elements.container;
}

async function refreshBody() {
  const favoriteModalElement = getElement("favoriteModal");
  const body = favoriteModalElement.querySelector(".modal-body");

  const likedPositions = getCookieOrFalse("likedPositions");
  const idsRaw = likedPositions ? JSON.parse(likedPositions) : [];

  if (idsRaw.length === 0) {
    body.textContent = "";
    return;
  }

  const ids = idsRaw.join(",");
  const response = await fetch(`/api/ids/?ids=${ids}&format=json`);
  const positions = await response.json();

  body.textContent = "";

  const elements = positions.map(positionData => createCard(positionData));

  elements.forEach(element => {
    body.appendChild(element);
  });
}

// Search-related functions
const buildResultItem = (url, name, weight) => {
  const baseUrl = (RESTAURANT) ? '/restaurant' : '';

  const link = document.createElement("a");
  link.href = `${baseUrl}${url}`;

  const container = document.createElement("div");
  container.classList.add("search-result-item");

  const inputGroup = document.createElement("div");
  inputGroup.classList.add("input-group", "show", "d-flex", "align-items-center", "justify-content-center");

  const searchIconWrapper = document.createElement("span");
  searchIconWrapper.classList.add("input-group-append", "text-white", "d-flex", "align-items-center");
  const searchIcon = document.createElement("span");
  searchIcon.classList.add("material-icons");
  searchIcon.textContent = "search";

  searchIconWrapper.appendChild(searchIcon);

  const titleContainer = document.createElement("span");
  titleContainer.classList.add("search-item-title", "d-flex", "align-items-center");
  titleContainer.style = "margin-left: 10px;";

  const menuItemTitle = document.createElement("span");
  menuItemTitle.textContent = name;
  titleContainer.appendChild(menuItemTitle);

  if (weight > 0) {
    const menuItemWeight = document.createElement("span");
    menuItemWeight.textContent = `${weight}`;
    menuItemWeight.classList.add("badge", "bg-dark");
    menuItemWeight.style = "margin-left: 10px;";
    titleContainer.appendChild(menuItemWeight);
  }

  inputGroup.appendChild(searchIconWrapper);
  inputGroup.appendChild(titleContainer);
  container.appendChild(inputGroup);
  link.appendChild(container);

  return link;
};

const loadResults = async () => {
  const nothingFounded = getElement("search-nothing");
  const items = getElement("search-items");
  items.textContent = "";

  const MIN_QUERY_LENGTH = 3;

  if (searchQuery.length < MIN_QUERY_LENGTH) {
    nothingFounded.classList.remove("d-none");
    return;
  }

  nothingFounded.classList.add("d-none");

  const baseUrl = (RESTAURANT) ? '/restaurant' : '';
  const urlToFetch = `${baseUrl}/api/search?q=${searchQuery}&format=json`;

  const response = await fetch(urlToFetch);
  const results = await response.json();

  if (results.length < 1) {
    nothingFounded.classList.remove("d-none");
  }

  results.forEach(result => {
    const { url, name, weight } = result;
    const resultItem = buildResultItem(url, name, weight);
    items.appendChild(resultItem);
  });
};

const updateQuery = (event) => {
  const { value } = event.target;
  searchQuery = value;

  loadResults();
};
