from js import document
from pyodide.ffi import create_proxy

# Lenape vocabulary from the document
lenape_examples = {
    "colors": """Colors in Lenape:
    seke (suhk-ay) = it is black
    ope = it is white
    askaskwe (uh-skuh-skway) = it is green
    aone = it is blue
    wipunkwe = it is gray
    wisae = it is yellow
    maxke = it is red""",
    
    "numbers": """Numbers in Lenape:
    kweti (kwuh-tee) = one
    nisha (nee-shah) = two""",
    
    "feelings": """Feelings in Lenape:
    mpalsi (bahl-see) = I am sick
    newikwihela (nuh-wee-kwee-huh-lah) = I am tired
    nkesi (guh-see) = I am hot
    ntakohchi (dah-koh-chee) = I am cold
    ku mayay (ku-my-eye) = not quite"""
}

def show_madlib1(event):
    container = document.getElementById("madlib-container")
    container.innerHTML = """
        <h2>The Bicycle Crash</h2>
        <div class="input-group">
            <label>Enter a body part:</label>
            <input type="text" id="bodypart1">
        </div>
        <!-- Add other input fields -->
        <button py-click="generate_story1">Generate Story!</button>
        <div id="story1-output"></div>
    """

def show_madlib2(event):
    container = document.getElementById("madlib-container")
    container.innerHTML = """
        <h2>Two to Tango</h2>
        <div class="input-group">
            <label>Enter a number:</label>
            <input type="text" id="number2">
        </div>
        <!-- Add other input fields -->
        <button py-click="generate_story2">Generate Story!</button>
        <div id="story2-output"></div>
    """

def setup_examples():
    container = document.getElementById("examples-container")
    for category, text in lenape_examples.items():
        button = document.createElement("button")
        button.textContent = f"{category.title()} Examples"
        button.onclick = create_proxy(lambda e, cat=category: toggle_example(cat))
        container.appendChild(button)
        
        div = document.createElement("div")
        div.id = f"example-{category}"
        div.style.display = "none"
        div.innerHTML = text.replace("\n", "<br>")
        container.appendChild(div)

def toggle_example(category):
    div = document.getElementById(f"example-{category}")
    div.style.display = "block" if div.style.display == "none" else "none"

setup_examples()