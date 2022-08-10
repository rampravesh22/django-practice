$(document).ready(function () {
    $(document).on('submit', '#form_id', function (e) {
        e.preventDefault();
        const name = $('#id_name').val();
        const subjects = $("#id_subjects").prop("checked");
        console.log(name);
        console.log(subjects);

        $.ajax({
            type: 'POST',
            url: '/',
            data: {
                name: name,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                console.log("Data saved successfully")
            },
        });
    });
});