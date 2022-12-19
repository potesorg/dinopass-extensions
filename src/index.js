import axios from "axios";
const api = "https://www.dinopass.com/password/strong";
const errors = document.querySelector(".errors");
const loading = document.querySelector(".loading");
const pass = document.querySelector(".pass");
const results = document.querySelector(".result-container");
results.style.display = "none";
loading.style.display = "none";
errors.textContent = "";
// grab the form
const form = document.querySelector(".form-data");
// grab the country name

// declare a method to search by country name
const generateStrongPass = async () => {
  loading.style.display = "block";
  // errors.textContent = "";
  try {
    const response = await axios.get(`${api}/`);
    loading.style.display = "none";
    pass.textContent = response.data;
    results.style.display = "block";
  } catch (error) {
    loading.style.display = "none";
    results.style.display = "none";
    errors.textContent = "Dinopass API call failed.";
  }
};

// declare a function to handle form submission
const handleSubmit = async e => {
  e.preventDefault();
  generateStrongPass();
};

const copyButtonLabel = "Copy";

// use a class selector if available
let blocks = document.querySelectorAll("pre");

blocks.forEach((block) => {
  // only add button if browser supports Clipboard API
  if (navigator.clipboard) {
    let br = document.createElement("span");
    br.innerHTML = "<br/>";
    let button = document.createElement("button");
    button.classList.add("ui");

    button.innerText = copyButtonLabel;
    br.appendChild(button);

    block.appendChild(br);
    button.addEventListener("click", async () => {
      await copyCode(block, button);
    });
  }
});

async function copyCode(block, button) {
  let code = block.querySelector("span.pass");
  let text = code.innerText;

  await navigator.clipboard.writeText(text);

  // visual feedback that task is completed
  button.innerText = "Copied to clipboard";

  setTimeout(() => {
    button.innerText = copyButtonLabel;
  }, 700);
}


form.addEventListener("submit", e => handleSubmit(e));
