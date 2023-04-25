// $(document).ready(function () {

// })


let addMulRowsDict = function(event) {
  event.preventDefault();
  const formData = $('#myForm').serializeArray();
  var rowsData = {};
  
  $.each(formData, function(index, field){
    rowsData[field.name] = field.value;
  });

  // for every field of checkbox just to be there
  $('input[type="checkbox"]').each(function(){
    rowsData[this.name] = false;
  })

  // only if true - rewrite (because there's 2 checkboxes - one on top of another)
  $('input[type="checkbox"]').each(function(){
    if ($(this).prop('checked') == true) {
      rowsData[this.name] = true;
    }
  });

  let checkData = JSON.stringify(rowsData);
  alert(checkData);
  console.log(checkData);
  return false;
}