'use strict';

var globChoice = {};
$(document).ready(function () {
  globChoice = getFromForm();
  activateSuggest();

  $("#select_custom").on('input', function() {
    autocomplete_suggest("#select_custom");
  });

});


let showAlwaysOpen = function () {
  $('body').on('click', function(event){
    event.stopPropagation();
    $("#4select").trigger('chosen:open');
  });
}

let changeOpts = function (btn) {
  console.log('changed');
}

let activateSuggest = function () {
  let search_exist = true;

  for (let item of ['#1select', '#2select', '#3select', '#4select'] ) {

    if ($(item).length > 0) { 
      $(item).chosen({ 
        width:'100%',
        disable_search: search_exist,
        inherit_select_classes: true,
        no_results_text: 'Нет совпадений'
      });
    }
  }
 
}

let renewFilters = function () {
  // selects with multiple choice, renew after each click
  globChoice = getFromForm();
  let checkData = JSON.stringify(globChoice);
  console.log(checkData);

  let callUrl = $.post({
    url: '/',
    data: { options: checkData },    // not stringified as a whole, but argument
  });

  callUrl.done(
    function (result) {
      $('#myForm').replaceWith(result);
      activateSuggest();
  })

  return false;
}

let unselectFromFilterOpts = function (btn) {
  let filterId = $(btn).parent().attr('data-name');
  let deleteVal = $(btn).attr('data-val');
  let el = $("#" + filterId);
  let newData = [];
  //TODO
  console.log(filterId)
  renewFilters();

}




let getFromForm = function () {
  let formData = $('#myForm').serializeArray();
  let rowsData = { '1select': [], '2select': [], '3select': [], 'single': [], '4select': [] };

  $.each(formData, function (index, field) {
    rowsData[field.name].push(field.value);
  });
  return rowsData
}



let loadSuggestsByInput = function (request, fieldName, response) {
      let input_ = request.term;
      var suggestUrl = "".concat('/suggest', '?query=', input_, 
                              '&field=', fieldName.substring(1));//, 
                              // '&region=', '1',
                              // '&settlement_id=', '2');
      $.ajax({
        url: suggestUrl,
        type: 'GET',
        success: function (data) {
          response(data);
        }
      })
}


// Отправка запроса о Suggest-подстановке
let autocomplete_suggest = function(fieldName) {
  console.log('autocomplete_suggest')
  var input_ = "";
  $(fieldName).autocomplete({
    delay: 300,
    minLength: 1,
    source: function (request, response) { 
      loadSuggestsByInput(request, fieldName, response);
    },
    select: function(event, ui) {
      $(fieldName).attr('value' , ui.item.label);
      $(fieldName).attr('data-id', ui.item.id);
      $('#custom_select').val(ui.item.label)
      // let elem = $("#region_select_m>.select_opt[data-val='" + ui.item.id + "']");
      // $('#select_region').val(ui.item.label);
      // if (elem.length > 0) {
      //   elem[0].scrollIntoView()
      //   elem.click();        
      // }
    }
  });
  $(fieldName).autocomplete( "option", "appendTo", ".ui-front" );
}

let changeOpt = function (btn) {
  $(btn).addClass('active');
  globChoice['suggest_form'] = $(btn).attr('data-id');
  loadList();
}


let loadList = function () {
  $.post({
    url: '/suggest/',
    data: JSON.stringify({ 'options': globChoice }),    // not stringified as a whole, but argument
  })
  .done(
    function (result) {
      console.log('loaded')
      $('#suggest_form').html(result);
     
  })
}