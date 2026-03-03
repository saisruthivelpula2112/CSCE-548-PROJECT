// script.js
const BASE = "http://127.0.0.1:9000";

// ── UI helpers ───────────────────────────────────────────────────────────────
function showStatus(msg) {
  const s = document.getElementById("statusBox");
  const e = document.getElementById("errorBox");
  s.textContent = "✅ " + msg; s.style.display = "block";
  e.style.display = "none";
}
function showError(msg) {
  const s = document.getElementById("statusBox");
  const e = document.getElementById("errorBox");
  e.textContent = "❌ " + msg; e.style.display = "block";
  s.style.display = "none";
}
function renderList(ulId, items, fmt) {
  const ul = document.getElementById(ulId);
  if (!items || items.length === 0) { ul.innerHTML = "<li><em>No records found.</em></li>"; return; }
  ul.innerHTML = items.map(i => `<li>${fmt(i)}</li>`).join("");
}
async function api(method, path, body) {
  const opts = { method, headers: { "Content-Type": "application/json" } };
  if (body) opts.body = JSON.stringify(body);
  const r = await fetch(BASE + path, opts);
  if (r.status === 204) return null;
  const data = await r.json();
  if (!r.ok) throw new Error(data.detail || r.statusText);
  return data;
}

// ── USERS ────────────────────────────────────────────────────────────────────
async function getUsers() {
  try {
    const data = await api("GET", "/users");
    renderList("userList", data, u => `id:${u.id} — ${u.username} — ${u.email} — ${u.role}`);
    showStatus(`Loaded ${data.length} user(s).`);
  } catch(e) { showError(e.message); }
}

async function getSingleUser() {
  const id = document.getElementById("getSingleUserId").value;
  if (!id) { showError("Enter a user id."); return; }
  try {
    const u = await api("GET", `/users/${id}`);
    renderList("singleUserResult", [u], u => `id:${u.id} — ${u.username} — ${u.email} — ${u.role}`);
    showStatus(`Found user id:${id}.`);
  } catch(e) { showError(e.message); }
}

async function createUser() {
  const username = document.getElementById("newUsername").value.trim();
  const email    = document.getElementById("newEmail").value.trim();
  if (!username || !email) { showError("Username and email required."); return; }
  try {
    await api("POST", "/users", { username, email, role: "student" });
    showStatus("User created successfully.");
    getUsers();
  } catch(e) { showError(e.message); }
}

async function updateUser() {
  const id    = document.getElementById("updateUserId").value;
  const email = document.getElementById("updateUserEmail").value.trim();
  if (!id || !email) { showError("User id and new email required."); return; }
  try {
    await api("PUT", `/users/${id}`, { email });
    showStatus("User updated successfully.");
    getUsers();
  } catch(e) { showError(e.message); }
}

async function deleteUser() {
  const id = document.getElementById("deleteUserId").value;
  if (!id) { showError("Enter a user id."); return; }
  if (!confirm(`Delete user id:${id}?`)) return;
  try {
    await api("DELETE", `/users/${id}`);
    showStatus(`User id:${id} deleted.`);
    getUsers();
  } catch(e) { showError(e.message); }
}

// ── PROJECTS ─────────────────────────────────────────────────────────────────
const fmtProject = p => `project_id:${p.project_id} — owner_id:${p.owner_id} — ${p.title}`;

async function getProjects() {
  try {
    const data = await api("GET", "/projects");
    renderList("projectList", data, fmtProject);
    showStatus(`Loaded ${data.length} project(s).`);
  } catch(e) { showError(e.message); }
}

async function getProjectsByOwner() {
  const id = document.getElementById("ownerFilterId").value;
  if (!id) { showError("Enter an owner id."); return; }
  try {
    const data = await api("GET", `/projects/owner/${id}`);
    renderList("projectSubset", data, fmtProject);
    showStatus(`Found ${data.length} project(s) for owner ${id}.`);
  } catch(e) { showError(e.message); }
}

async function getSingleProject() {
  const id = document.getElementById("getSingleProjectId").value;
  if (!id) { showError("Enter a project id."); return; }
  try {
    const p = await api("GET", `/projects/${id}`);
    renderList("singleProjectResult", [p], fmtProject);
    showStatus(`Found project id:${id}.`);
  } catch(e) { showError(e.message); }
}

async function createProject() {
  const owner_id = parseInt(document.getElementById("newProjectOwner").value);
  const title    = document.getElementById("newProjectTitle").value.trim();
  if (!owner_id || !title) { showError("Owner id and title required."); return; }
  try {
    await api("POST", "/projects", { owner_id, title });
    showStatus("Project created successfully.");
    getProjects();
  } catch(e) { showError(e.message); }
}

async function deleteProject() {
  const id = document.getElementById("deleteProjectId").value;
  if (!id) { showError("Enter a project id."); return; }
  if (!confirm(`Delete project id:${id}?`)) return;
  try {
    await api("DELETE", `/projects/${id}`);
    showStatus(`Project id:${id} deleted.`);
    getProjects();
  } catch(e) { showError(e.message); }
}

// ── ITEMS ─────────────────────────────────────────────────────────────────────
const fmtItem = i => `item_id:${i.item_id} — project_id:${i.project_id} — ${i.name}`;

async function getItems() {
  try {
    const data = await api("GET", "/items");
    renderList("itemList", data, fmtItem);
    showStatus(`Loaded ${data.length} item(s).`);
  } catch(e) { showError(e.message); }
}

async function getItemsByProject() {
  const id = document.getElementById("itemProjectFilter").value;
  if (!id) { showError("Enter a project id."); return; }
  try {
    const data = await api("GET", `/items/project/${id}`);
    renderList("itemSubset", data, fmtItem);
    showStatus(`Found ${data.length} item(s) for project ${id}.`);
  } catch(e) { showError(e.message); }
}

async function getSingleItem() {
  const id = document.getElementById("getSingleItemId").value;
  if (!id) { showError("Enter an item id."); return; }
  try {
    const item = await api("GET", `/items/${id}`);
    renderList("singleItemResult", [item], fmtItem);
    showStatus(`Found item id:${id}.`);
  } catch(e) { showError(e.message); }
}

async function createItem() {
  const project_id = parseInt(document.getElementById("newItemProject").value);
  const name       = document.getElementById("newItemName").value.trim();
  if (!project_id || !name) { showError("Project id and name required."); return; }
  try {
    await api("POST", "/items", { project_id, name });
    showStatus("Item created successfully.");
    getItems();
  } catch(e) { showError(e.message); }
}

async function deleteItem() {
  const id = document.getElementById("deleteItemId").value;
  if (!id) { showError("Enter an item id."); return; }
  if (!confirm(`Delete item id:${id}?`)) return;
  try {
    await api("DELETE", `/items/${id}`);
    showStatus(`Item id:${id} deleted.`);
    getItems();
  } catch(e) { showError(e.message); }
}

// ── TAGS ──────────────────────────────────────────────────────────────────────
const fmtTag = t => `tag_id:${t.tag_id} — ${t.tag_name}`;

async function getTags() {
  try {
    const data = await api("GET", "/tags");
    renderList("tagList", data, fmtTag);
    showStatus(`Loaded ${data.length} tag(s).`);
  } catch(e) { showError(e.message); }
}

async function getSingleTag() {
  const id = document.getElementById("getSingleTagId").value;
  if (!id) { showError("Enter a tag id."); return; }
  try {
    const tag = await api("GET", `/tags/${id}`);
    renderList("singleTagResult", [tag], fmtTag);
    showStatus(`Found tag id:${id}.`);
  } catch(e) { showError(e.message); }
}

async function createTag() {
  const tag_name = document.getElementById("newTagName").value.trim();
  if (!tag_name) { showError("Tag name required."); return; }
  try {
    await api("POST", "/tags", { tag_name });
    showStatus("Tag created successfully.");
    getTags();
  } catch(e) { showError(e.message); }
}

async function deleteTag() {
  const id = document.getElementById("deleteTagId").value;
  if (!id) { showError("Enter a tag id."); return; }
  if (!confirm(`Delete tag id:${id}?`)) return;
  try {
    await api("DELETE", `/tags/${id}`);
    showStatus(`Tag id:${id} deleted.`);
    getTags();
  } catch(e) { showError(e.message); }
}

// ── ITEM TAGS ─────────────────────────────────────────────────────────────────
const fmtItemTag = it => `item_id:${it.item_id} — tag_id:${it.tag_id} — ${it.item_name || ""} — ${it.tag_name}`;

async function getItemTags() {
  try {
    const data = await api("GET", "/item_tags");
    renderList("itemTagList", data, fmtItemTag);
    showStatus(`Loaded ${data.length} item-tag link(s).`);
  } catch(e) { showError(e.message); }
}

async function getTagsForItem() {
  const id = document.getElementById("itemTagFilter").value;
  if (!id) { showError("Enter an item id."); return; }
  try {
    const data = await api("GET", `/item_tags/${id}`);
    renderList("itemTagSubset", data, it => `item_id:${it.item_id} — tag_id:${it.tag_id} — ${it.tag_name}`);
    showStatus(`Found ${data.length} tag(s) for item ${id}.`);
  } catch(e) { showError(e.message); }
}

async function addItemTag() {
  const item_id = parseInt(document.getElementById("linkItemId").value);
  const tag_id  = parseInt(document.getElementById("linkTagId").value);
  if (!item_id || !tag_id) { showError("Item id and tag id required."); return; }
  try {
    await api("POST", "/item_tags", { item_id, tag_id });
    showStatus(`Tag ${tag_id} linked to item ${item_id}.`);
    getItemTags();
  } catch(e) { showError(e.message); }
}

async function removeItemTag() {
  const item_id = document.getElementById("unlinkItemId").value;
  const tag_id  = document.getElementById("unlinkTagId").value;
  if (!item_id || !tag_id) { showError("Item id and tag id required."); return; }
  if (!confirm(`Remove tag ${tag_id} from item ${item_id}?`)) return;
  try {
    await api("DELETE", `/item_tags/${item_id}/${tag_id}`);
    showStatus(`Tag ${tag_id} removed from item ${item_id}.`);
    getItemTags();
  } catch(e) { showError(e.message); }
}