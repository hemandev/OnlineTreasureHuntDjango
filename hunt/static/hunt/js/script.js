/**
 * Created by HEMANDS on 24-02-2017.
 */



$(document).ready(function () {

    console.log("hello world!");


    $("#form").submit(function (e) {
        e.preventDefault();



        var answer = $("#answer").val();

        $.ajax({

            url: '/check_answer/',

            type: 'POST',

            data: {'answer': answer,'csrfmiddlewaretoken': CSRF_TOKEN},

            dataType: 'json',

            success: function (json) {
                if (json.answer) {

                    console.log("Success!");
                    $("#mymodal").modal('toggle');
                    $(".modal-header h1").text("Correct Answer");
                    $(".modal-body img").attr("src",'/static/hunt/images/correct.jpg');
                    $(".modal-footer button").text("Next")
                                        .click(function () {
                                            location.reload();
                                        });




                }

                else{

                    $("#mymodal").modal('toggle');
                    $(".modal-header h1").text("Wrong Answer");
                    $(".modal-body img").attr("src",'/static/hunt/images/wrong.jpg');
                    $(".modal-footer button").text("Try Again")



                }


            },

            error: function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }


        });

    });


});






