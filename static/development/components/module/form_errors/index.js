// підгружає стилі 
import './index.scss'
// імортує валідацію для номерів оператора
// import {check_operator} from '../mob_operator/index';

// до класу додає маску для телефону
$('input[type="tel"]').mask("+38(099) 999 9999");
// створюється масив з усіма операторами

// загальна функція яка загружається при загрузці сторінки
$(function () {
  Onload();
})

// в цю функцію заганяються форми які мають проходити валідацію
function Onload() {
  valide_form('.form__block', '.input', true);
  valide_form('.form_consultation', '.input', true);
}
// вертає конкретну мову, яка стоїть зараз на сайті
function location_leng() {
  return location.pathname.split('/')[1];
}
// основна функція, яка валідує потрібну форму
function valide_form(id_form, append_error_box, check_request) {
  var check_request = check_request;
  if ($(id_form).length > 0) {

    var lang_site;
    var errore_text = {};

    lang_site = location_leng();
    // перевіряє мову сайту, і вертає потрібний переклад
    switch (lang_site) {
      case 'uk':
        errore_text.required = 'Поле обов\'язково для заповнення';
        errore_text.email = 'Поле має містити email';
        errore_text.min_pass = 'Пароль занадто короткий';
        break;
      case 'ru':
        errore_text.required = 'Поле обязательно для заполнения';
        errore_text.email = 'Поле должно содержать email';
        errore_text.min_pass = 'Пароль слишком краток';

        break;
      case 'en':
        errore_text.required = 'The field is required';
        errore_text.email = 'The field must contain an email';
        errore_text.min_pass = 'Password is too short';

        break;
      default:
        errore_text.required = 'Поле обов\'язково для заповнення';
        errore_text.email = 'Поле має містити email';
        errore_text.min_pass = 'Пароль занадто короткий';


    }

    // функція самого плагіну
    $(id_form).validate({
      errorPlacement: function (event, validator) {

        $(validator).parents(append_error_box).append($(event));
        $(validator).parents(append_error_box).addClass('is-error')
      },
      rules: {
        name: {
          required: true,
        },
        message: {
          required: true,
        },
        phone: {
          required: true,
        },
      },

      messages: {
        name: {
          required: errore_text.required,
        },
        message: {
          required: errore_text.required,
        },
        phone: {
          required: errore_text.required,
        },
      },

      submitHandler: function (form) {
        event.preventDefault();
        $('.load_spin').addClass('load_spin_active');

        let Formdata = new FormData();
        var form_input = $(form).serializeArray();
        var url_form = form.action;
        var form_json = {};
        $(form_input).each(function (index, obj) {
          form_json[obj.name] = obj.value;
        });

        let user_files = form.querySelectorAll('#input_user_file')[0];

        if (user_files != undefined) {
          if (user_files.files[0] !== undefined) {
            $.each(user_files.files, function (index, value) {
              Formdata.append('file', value);
            });
          }
        }

        Formdata.append('data', JSON.stringify(form_json));

        if (url_form != '') {

          fetch(url_form, {
            method: 'POST',
            body: Formdata,
          })
            .then(data => {
              return data.json();
            })
            .then(data => {
              console.log('typeof data', typeof data['status']);
              console.log('data.status: ', data.status);
              if (data.status == 'OK' && typeof data['status'] !== "undefined") {

                sayHi();
              } else {

                // if(data.status=='BAD' && typeof data['status'] !== "undefined"){

              }

              if (typeof data['url'] !== "undefined" && data.url != '') {
                //   sayHi();
                location.href = data.url;
              }



            })
            .catch(err => {
              console.log('err: ', err);
              $('.load_spin').removeClass('load_spin_active');
              $.fancybox.open({
                src: '#modal-form_true',
              });
              $('.error_form').css('display', 'inline-block');
              $('.form_true_img').css('display', 'none');
              $('.usually_modal_text').text('Вибачте, сталась помилка. Спробуйте пізніше.');
              setTimeout(() => {
                $.fancybox.close();
                $.fancybox.close({
                  src: '#modal-form_true',
                });

              }, 1500);
              setTimeout(() => {
                $('.form_true_img').css('display', 'inline-block');
                $('.error_form').css('display', 'none');
                $('.usually_modal_text').text('Дякуємо, заявка опрацьована. Наші менеджери звяжуться з Вами');
              }, 2500);
            });

        } else {
          console.log("forn_not_actions");
        }



        function sayHi() {
          $('.load_spin').removeClass('load_spin_active');
          if (check_request === true) {
            $.fancybox.open({
              src: '#modal-form_true',
            });
            setTimeout(() => {
              $.fancybox.close();
              $.fancybox.close({
                src: '#modal-form_true',
              });
            }, 1500);
            var form_inputs = $(form)[0].querySelectorAll('input');
            if (form_inputs.length > 0) {
              for (var key in form_inputs) {
                if (form_inputs.hasOwnProperty(key) && /^0$|^[1-9]\d*$/.test(key) && key <= 4294967294) {
                  if (form_inputs[key].type == 'hidden') {

                  } else if (form_inputs[key].type !== 'submit') {
                    form_inputs[key].value = '';
                  }

                }
              }
              var form_textaria = $(form)[0].querySelectorAll('textarea');
              if (form_textaria.length > 0) {
                form_textaria[0].value = '';
              }
            }
          }
        }

      }

    });
  }

}

