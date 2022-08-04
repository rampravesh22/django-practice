$(document).ready(function () {
    $(document).on('submit', '#form_id', function (e) {
        console.log("hello world");
        e.preventDefault();
        const name = $('#name_id').val();
        const email = $('#email_id').val();
 
        $.ajax({
            type: 'POST',
            url: 'getemail/',
            data: {
                name: name,
                email: email,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                cosole.log("Data saved successfully")
            },
        });
    });
});