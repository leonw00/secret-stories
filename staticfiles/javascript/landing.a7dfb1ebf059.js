
  
$(document).ready(function() {
    
    $(window).scroll( function(){
    
        $('.iconbox').each( function(i){
            
            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            
            if( bottom_of_window > bottom_of_object ){
                $(this).animate({'opacity':'1'},550);
            }
            
        }); 

        $('.questioncontainer').each( function(i){

            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            
            if( bottom_of_window > bottom_of_object ){
                $(this).animate({'opacity':'1'},1400);
            }
            
        }); 
    
    });
    
});


let collapsible = document.getElementsByClassName('collapsible');
let arrowImage = document.getElementsByClassName('arrow');
for(let i = 0; i < collapsible.length; i++){
    collapsible[i].addEventListener('click', function(){
        this.classList.toggle("activate");
        let content = this.nextElementSibling;
        if(content.style.maxHeight != 0){
            content.style.maxHeight = null;
            collapsible[i].classList.remove("colactive");
            arrowImage[i].classList.remove("arrowactive");
        }
        else{
            content.style.maxHeight = content.scrollHeight + "px";
            collapsible[i].classList.add("colactive");
            arrowImage[i].classList.add("arrowactive");
        }
    })
}