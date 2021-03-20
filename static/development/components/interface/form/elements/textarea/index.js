import './index.scss'

let field_inputs = $('.input-field');
if (field_inputs.length > 0) {
    field_inputs.on('focus', function () {
        $(this).parents('.input').addClass('in-focus');
        $(this).parents('.input').removeClass('is-error');
    })
    field_inputs.on('blur', function () {
        if ($(this).val().length < 1 || $(this).val() == '+38(___) ___-____') {
            $(this).parents('.input').removeClass('in-focus')
        }
    })
    $('.form__group_label').on('click', function () {
        $(this).parents('.input').toggleClass('in-focus')
    })

    for (const key in field_inputs) {
        if (field_inputs.hasOwnProperty(key) && typeof field_inputs[key] == 'object') {
            let input = field_inputs[key];

            if ($(input).val().length > 1) {
                $(input).parents('.textarea').addClass('in-focus')
            } else {
                $(input).parents('.textarea').removeClass('in-focus')
            }
        }
    }
}