$(document).ready(function () {
    $(document).on('submit', '#add-student', function (e) {
        console.log("hello world");
        const name = $('#id_name').val();
        const age = $('#id_age').val();
        const gender = $('#id_gender').val();
 
        $.ajax({
            type: 'POST',
            url: '/',
            data: {
                name: name,
                age: age,
                gender:gender,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                console.log(response);
                window.location.href="edit/"
            },
        });
    });
});