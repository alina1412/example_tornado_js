$(document).ready(function () {
  // https://snipp.ru/jquery/time-ui-datepicker
  /* Локализация datepicker */
  $.datepicker.regional['ru'] = {
    closeText: 'Закрыть',
    prevText: 'Предыдущий',
    nextText: 'Следующий',
    currentText: 'Сегодня',
    monthNames: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
    monthNamesShort: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
    dayNames: ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота'],
    dayNamesShort: ['вск', 'пнд', 'втр', 'срд', 'чтв', 'птн', 'сбт'],
    dayNamesMin: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
    weekHeader: 'Не',
    dateFormat: 'dd.mm.yy',
    firstDay: 1,
    isRTL: false,
    showMonthAfterYear: false,
    yearSuffix: ''
  };
  $.datepicker.setDefaults($.datepicker.regional['ru']);

  /* Локализация timepicker */
  $.timepicker.regional['ru'] = {
    timeOnlyTitle: 'Выберите время',
    timeText: 'Время',
    hourText: 'Часы',
    minuteText: 'Минуты',
    // secondText: 'Секунды',
    // millisecText: 'Миллисекунды',
    timezoneText: 'Часовой пояс',
    currentText: 'Сейчас',
    closeText: 'Закрыть',
    timeFormat: 'HH:mm',
    amNames: ['AM', 'A'],
    pmNames: ['PM', 'P'],
    isRTL: false
  };
  $.timepicker.setDefaults($.timepicker.regional['ru']);

  var myControl = {
    create: function (tp_inst, obj, unit, val, min, max, step) {
      $('<input class="ui-timepicker-input" value="' + val + '" style="width:50%">')
        .appendTo(obj)
        .spinner({
          min: min,
          max: max,
          step: step,
          change: function (e, ui) {
            if (e.originalEvent !== undefined)
              tp_inst._onTimeChange();
            tp_inst._onSelectHandler();
          },
          spin: function (e, ui) {
            tp_inst.control.value(tp_inst, obj, unit, ui.value);
            tp_inst._onTimeChange();
            tp_inst._onSelectHandler();
          }
        });
      return obj;
    },
    options: function (tp_inst, obj, unit, opts, val) {
      if (typeof (opts) == 'string' && val !== undefined)
        return obj.find('.ui-timepicker-input').spinner(opts, val);
      return obj.find('.ui-timepicker-input').spinner(opts);
    },
    value: function (tp_inst, obj, unit, val) {
      if (val !== undefined)
        return obj.find('.ui-timepicker-input').spinner('value', val);
      return obj.find('.ui-timepicker-input').spinner('value');
    }
  };

  $(function () {
    $("#date").datetimepicker({
      controlType: myControl,
      showOn: "button",
      buttonImage: "https://snipp.ru/demo/437/calendar.gif",
      buttonImageOnly: true,
      buttonText: "Выбрать дату"
    });
  });
})


let validateTime = function (time, element) {
  if (time.length < 5) {
    element.addClass('border-danger');
    return false;
  }
  let timeRegex = /^([01][0-9]|2[0-3]):([0-5][0-9])$/;
  res = timeRegex.test(time);
  if (res) {
    element.removeClass('border-danger');
  }
  else {
    element.addClass('border-danger');
  }
  return res;
}


let validateDate = function (date, element) {
  if (date.length < 10) {
    element.addClass('border-danger');
    return false;
  }
  date = date.substring(0, 2) + "/" + date.substring(3, 5) + "/" + date.substring(6, 10)
  let dateRegex = /^(?=\d)(?:(?:31(?!.(?:0?[2469]|11))|(?:30|29)(?!.0?2)|29(?=.0?2.(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00)))(?:\x20|$))|(?:2[0-8]|1\d|0?[1-9]))([-.\/])(?:1[012]|0?[1-9])\1(?:1[6-9]|[2-9]\d)?\d\d(?:(?=\x20\d)\x20|$))?(((0?[1-9]|1[012])(:[0-5]\d){0,2}(\x20[AP]M))|([01]\d|2[0-3])(:[0-5]\d){1,2})?$/;
  // console.log(dateRegex.test('21/01/1986'));
  // console.log( '-------')
  res = dateRegex.test(date);
  if (res) {
    element.removeClass('border-danger');
  }
  else {
    element.addClass('border-danger');
  }
  return res;
}


let checkDate = function (event) {
  let startDate = $('#date').val();
  if (startDate) {
    if (validateDate(startDate.substring(0, 10), $('#date'))) {
      alert('y')
    }
    else {
      alert('no')
    }

    if (validateTime(startDate.substring(11, 17), $('#date'))) {
      alert('y')
    }
    else {
      alert('no -  ' + startDate.substring(11, 17));
    }
  }
  event.preventDefault()
  return false;
}

