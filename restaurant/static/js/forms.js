const getFormFields = (fieldIds, prefix = "id_") => {
  const fields = {};
  fieldIds.forEach(fieldName => {
    fields[fieldName] = document.getElementById(prefix + fieldName);
  });
  return fields;
};

const fillForm = (formData, fieldIds, prefix = "id_") => {
  const fields = getFormFields(fieldIds, prefix);

  for (const [fieldName, field] of Object.entries(fields)) {
    field.value = formData[fieldName];
    if (field.type === 'checkbox') field.checked = formData[fieldName];
  }
};

const fillCreateForm = subcategoryId => {
  const fieldIds = ["subcategory_position_create", "priority_position_create"];
  const formData = {
    subcategory_position_create: subcategoryId,
    priority_position_create: "1",
  };

  fillForm(formData, fieldIds);
};

const fillCreateSubcategoryForm = (category) => {
  const fieldIds = [
    "name_subcategory_create",
    "priority_subcategory_create",
  ];
  const formData = {
    name_subcategory_create: "",
    category_subcategory_create: category,
    priority_subcategory_create: 1,
  };

  fillForm(formData, fieldIds);
};

const fillSubcategoryEditForm = (name, priority, category, id) => {
  const fieldIds = [
    "id_subcategory_edit",
    "name_subcategory_edit",
    "priority_subcategory_edit",
    "category_subcategory_edit",
  ];
  const formData = {
    id_subcategory_edit: parseInt(id),
    name_subcategory_edit: name,
    priority_subcategory_edit: priority,
    category_subcategory_edit: category,
  };

  fillForm(formData, fieldIds);
};

const fillEditForm = positionId => {
  const fieldIds = [
    "subcategory_position_edit",
    "priority_position_edit",
    "name_position_edit",
    "spiciness_position_edit",
    "weight_position_edit",
    "description_position_edit",
    "is_new_position_edit",
    "price_position_edit",
    "cooking_time_position_edit",
    "id_position_edit",
    "active_position_edit",
  ];
  const position = document.getElementById(`position-${positionId}`);
  const formData = {
    active_position_edit: position.dataset.positionActive === "True",
    name_position_edit: position.dataset.positionName,
    subcategory_position_edit: position.dataset.positionSubcategory,
    description_position_edit: position.dataset.positionDescription,
    price_position_edit: position.dataset.positionPrice,
    spiciness_position_edit: position.dataset.positionSpiciness,
    weight_position_edit: position.dataset.positionWeight,
    cooking_time_position_edit: position.dataset.positionCookingTime,
    id_position_edit: position.dataset.positionId,
    priority_position_edit: position.dataset.positionPriority,
    is_new_position_edit: position.dataset.positionIsNew === "True",
  };

  fillForm(formData, fieldIds);
};

function submitSubcategoryCreate() {
  const form = document.getElementById("subcategoryCreateForm");
  const formData = new FormData(form);
  submitRequest(`${window.location.origin}${BASE_URL}/api/subcategories/`, "POST", formData, () => location.reload());
}

function submitSubcategoryEdit() {
  const form = document.getElementById("subcategoryChangeForm");
  const formData = new FormData(form);
  const subcategoryId = document.getElementById("id_id_subcategory_edit").value;
  submitRequest(`${window.location.origin}${BASE_URL}/api/subcategories/${subcategoryId}/`, "PATCH", formData, () => location.reload());
}

function submitCategoryChange() {
  const form = document.getElementById("categoryChangeForm");
  const formData = new FormData(form);
  submitRequest(`${window.location.origin}${BASE_URL}/api/categories/${formData.get("id")}/`, "PATCH", formData, () => location.reload());
}

function submitСategoryDeletion() {
  const categoryId = document.getElementById("id_id_category_edit").value;
  submitRequest(`${window.location.origin}${BASE_URL}/api/categories/${categoryId}/delete/`, "DELETE", null, () => document.location.href = "/");
}

function submitSubcategoryDeletion() {
  const form = document.getElementById("subcategoryChangeForm");
  const formData = new FormData(form);
  const subcategoryId = document.getElementById("id_id_subcategory_edit").value;
  submitRequest(`${window.location.origin}/api/subcategories/${subcategoryId}/delete/`, "DELETE", formData, () => location.reload());
}

function submitDeletion() {
  const form = document.getElementById("positionEditForm");
  const formData = new FormData(form);
  const positionId = formData.get("id");
  submitRequest(`${window.location.origin}${BASE_URL}/api/position/${positionId}/delete/`, "DELETE", formData, () => location.reload());
}

function submitFormEdit() {
  const form = document.getElementById("positionEditForm");
  const formData = new FormData(form);
  if (formData.get("image").size === 0) formData.delete("image");
  formData.append("is_new", document.getElementById("id_is_new_position_edit").checked);
  formData.append("is_active", document.getElementById("id_active_position_edit").checked);
  const positionId = formData.get("id");
  submitRequest(`${window.location.origin}${BASE_URL}/api/position/${positionId}/`, "PATCH", formData, () => location.reload());
}

function submitFormCreation() {
  const form = document.getElementById("positionCreateForm");
  const formData = new FormData(form);
  submitRequest(`${window.location.origin}${BASE_URL}/api/position/`, "POST", formData, () => location.reload());
}

document.addEventListener("DOMContentLoaded", () => {
  function toggleFullImage(positionId, action) {
    const position = document.querySelector(`${positionId}`);
    position.classList[action]("full-image");
  }

  function handleImageClick(e) {
    const positionId = e.target.dataset.positionId;
    toggleFullImage(positionId, (e.target.classList.contains("thumbnail") ? "add" : "remove"));
  }

  const thumbnails = document.querySelectorAll(".thumbnail");
  const fullImages = document.querySelectorAll(".position-image");

  thumbnails.forEach(thumbnail => {
    thumbnail.addEventListener("click", handleImageClick);
  });

  fullImages.forEach(fullImage => {
    fullImage.addEventListener("click", handleImageClick);
  });
});
