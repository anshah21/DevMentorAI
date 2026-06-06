document.getElementById("fileInput")
.addEventListener("change", function(e){

    const file = e.target.files[0];

    if(!file) return;

    const reader = new FileReader();

    reader.onload = function(event){
        document.getElementById("code").value =
        event.target.result;
    };

    reader.readAsText(file);
});

async function reviewCode(){

    const code =
    document.getElementById("code").value;

    const language =
    document.getElementById("language").value;

    document.getElementById("result").innerHTML =
'<div class="spinner"></div><p>Analyzing Code...</p>';

    try{

        const response = await fetch(
        "http://127.0.0.1:5000/review",
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                code:code,
                language:language
            })
        });

        const data = await response.json();

        document.getElementById("result").innerHTML =
marked.parse(data.review);

        document.getElementById("learning").innerHTML =
        `
        ✅ Study loops and conditions<br>
        ✅ Practice debugging syntax errors<br>
        ✅ Learn complexity analysis<br>
        ✅ Solve coding problems daily
        `;

    }
    catch(error){

        console.error(error);

        document.getElementById("result").innerHTML =
        "❌ Backend connection failed.";

    }
}

const codeArea = document.getElementById("code");
const languageSelect = document.getElementById("language");

function updateStats(){

    const code = codeArea.value;

    const lines =
    code.trim() === ""
    ? 0
    : code.split("\n").length;

    const chars = code.length;

    document.getElementById("lineCount").innerText =
    lines;

    document.getElementById("charCount").innerText =
    chars;

    document.getElementById("langDisplay").innerText =
    languageSelect.value;
}

codeArea.addEventListener("input", updateStats);

languageSelect.addEventListener("change", updateStats);

updateStats();