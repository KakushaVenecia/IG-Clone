let toggle = true;
document.addEventListener("DOMContentLoaded", (event)=>{
    console.log("hey")
    const j = document.querySelector("profile")
    j.addEventListener("click", ()=>{
        if(toggle === false){
            document.querySelector(".drop-down").getElementsByClassName.visibility = "hidden"
            
            toggle = true;

        }
        else if (toggle === true){
            document.querySelector(".profile").getElementsByClassName.visibility = "visible"
            document.querySelector(".drop-down").getElementsByClassName.visibility = "visible"
            toggle = false;

        }
    })
})