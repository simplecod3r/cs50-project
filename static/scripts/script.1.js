document.addEventListener('DOMContentLoaded', function(){

    let logo_ = document.querySelector('.logo_');
        logo_.addEventListener('click', ()=>{
            window.location.assign("index.html");
            // console.log("Cheguei aqui!")
        })
    
    let buttons = document.querySelectorAll('.button_');
    for (let i = 0; i < buttons.length; i++){
        buttons[i].addEventListener('click', function(){
            // console.log("Cheguei aqui!")
            // window.location.assign("/ps4-page.html")

            let console_ = buttons[i].innerHTML;
            console.log(console_);

            if (console_ === "PS4"){
                window.location.assign("ps4.html")
            }
            else if (console_ === "XBOX"){
                window.location.assign("xbox.html")
            }
            else if (console_ === "SWITCH"){
                window.location.assign("switch.html")
            }
            else if (console_ === "STEAM"){
                window.location.assign("steam.html")
            }
        });
    }
})