// AI Career Coach Interactive Effects



document.addEventListener(

"DOMContentLoaded",

function(){



    // Fade animation for cards


    const cards = document.querySelectorAll(

        ".result-card, .stat-card, .career-card, .feature-card"

    );



    cards.forEach(

        function(card,index){



            card.style.opacity="0";


            card.style.transform=

            "translateY(40px)";




            setTimeout(

                function(){



                    card.style.transition=

                    "all .7s ease";



                    card.style.opacity="1";



                    card.style.transform=

                    "translateY(0)";



                },

                index * 120

            );



        }

    );









    // Upload loading effect


    const form = document.querySelector("form");



    if(form){



        form.addEventListener(

            "submit",

            function(){



                const button =

                document.querySelector("button");




                if(button){



                    button.innerHTML=

                    "🧠 AI Analyzing Resume...";



                    button.style.opacity="0.7";



                    button.disabled=true;



                }



            }

        );



    }









    // Animated percentage scores



    const scoreElements =

    document.querySelectorAll(

        ".stat-card strong"

    );




    scoreElements.forEach(

        function(element){



            let target =

            parseInt(

                element.innerText

            );



            if(!isNaN(target)){



                let count=0;



                element.innerText="0%";




                let timer=setInterval(

                    function(){



                        count++;



                        element.innerText=

                        count+"%";





                        if(count>=target){



                            clearInterval(timer);



                        }




                    },

                    20

                );



            }



        }

    );





});