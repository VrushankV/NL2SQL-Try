
(function ($) {
    "use strict";

      /******

               Author : Sanni Michael Tomiwa 
                        Animashaun Abdul Azeem  

     ******/

      /******* Listen for click event on the convert button and run convertQuery function ******/
    document.getElementById('query').addEventListener('click', convertQuery);

    function convertQuery(){

        console.log("Hello");
        var name = document.getElementById("name").value;
        var message = document.getElementById("message").value;

        if(!name || !message) {
            swal("Please fill all fields !!!", "", "error");
            return;
        }
        else {
            // alert('Query Conversion in process.Thank you')
            $("#exampleModalCenter").modal("toggle");

          /******* Empty Form fields ******/
            document.getElementById("name").value = "";
            document.getElementById("message").value = "";
        }

    }
    
    

})(jQuery);