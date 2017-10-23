// Get all the elements we'll need later.
builder = document.getElementsByClassName("builder")[0];
form = builder.getElementsByTagName("form")[0];
age = document.getElementsByName("age")[0];
rel = document.getElementsByName("rel")[0];
smoker = document.getElementsByName("smoker")[0];
household = document.getElementsByClassName("household")[0];
debug = document.getElementsByClassName("debug")[0];
// Submit button doesn't have an easy handle. Loop and catch.
var nodeList = document.getElementsByTagName("button");
for ( item in nodeList ) {
    if(nodeList[item].type == "submit") {
        submit_btn = nodeList[item]
    };
};
add_btn = document.getElementsByClassName("add")[0];
jsonObj = {
    household:{}
};

// Add event listeners to everything.
add_btn.addEventListener("click", add_person);
submit_btn.addEventListener("click", submit_household);
age.setAttribute("onkeyup", "validate()");
rel.setAttribute("onchange", "validate()");

// Create a message p for validation warnings.
warn = document.createElement("p");
builder.appendChild(warn);

function add_person(){
    // Add people to a growing household list
    if ( validate() == false ) {
        event.preventDefault();
        return false;
    };
    person = document.createElement("li");
    if (smoker.checked) {
        smoke = "smoker";
    } else {
        smoke = "non-smoker";  
    };
    person.innerHTML = age.value + " " + rel.value + " " + smoke + " ";
    household.appendChild(person);
    // Create remove_person button, attach event listener.
    remove_btn = document.createElement("button");
    remove_btn.setAttribute("class", "remove");
    remove_btn.innerHTML = "x";
    remove_btn.addEventListener("click", remove_person);
    person.appendChild(remove_btn);
    event.preventDefault();
};

function remove_person(){
    // Remove a previously added person from the list
    // Get the li for this button.
    person = this.parentElement;
    // Remove the li from the DOM
    person.remove();
    event.preventDefault();
};

function submit_household() {
    // Start with an empty jsonObj
    jsonObj = {
        household:{}
    };
    // Check for empty household.
    if ( household.childElementCount > 0 ){
        // Get all the li values from the ol.
        var members = household.children;
        for ( var i = 0; i < members.length; i++ ) {
            var member = members[i].innerText;
            // Strip the 'x' remove button.
            member = member.replace(" x","");
            // Recapture values
            member =  member.split(" ");
            var age = member[0];
            var rel = member[1];
            var smoker = member[2];
            // Serialize the value to JSON.
            var j={
                "age":age, // FIX this!
                "relationship":rel,
                "smoker":smoker
            };
            jsonObj.household[i] = j;
        };
    } else {
        warn.innerText = "You didn't provide any members!";
    }

    // Add items to debug element.
    debug.innerText = JSON.stringify(jsonObj);
    debug.style.display = "inline";
    event.preventDefault();
};

function validate() {
    warn.innerHTML = "";
    // Age is required and > 0.
    input = age.value;
    var isInt = /^\+?\d+$/.test(input);
    if ( isInt == false || input == 0 ) {
        warn.innerHTML = "Age must be a positive number.";
        return false;
    };
    // Relationship is required.
    if ( rel.value == "" ) {
        warn.innerHTML = "Relationship must be provided.";
        return false;
    }
};
