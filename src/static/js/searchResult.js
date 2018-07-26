/**
 * Necessary actions when page is loaded: handler of click action for buttons
 * 
 * @return {bool} 
 */
$(document).ready(function() {
  $('#btn_search').click(function() {
    search_by_ingredient();
    return false;
  });

  $('#btn_add').click(function() {
    add_ingredient();
    return false;
  });

  $('#ingredientsList').on("click", "button", function(event) {
    delete_ingredient(event, this);
    return false;
  });
 
});


/**
 * Gets list of ingredients from form, sends request data
 * to backend, gets results and shows them in table
 */
function search_by_ingredient() {

  var post_data = {};
  $("li").map(function(id) {
    post_data['ingredient'+id] = $(this).text().slice(0, -1);
  });

  $.post('/search', post_data)
    .done(function(data) {
    $('#dishTable tbody').empty();
    for(var i = 0; i < data.length; i++){
       $('tbody').append(drawRow(data[i]));
    }
    
  });
}

/**
 *Forms list of ingredients
 */
function add_ingredient() {
   var ingredient = $('#ingredient').val();
   console.log(ingredient);
   var ingr_array = [];

   if (ingr_array.includes(ingredient) === false ) {
       ingr_array.push(ingredient);
       
       list_item = '<li>'+ ingredient;
       delete_btn = '<button type="button" class="close">' + 
                    '<span aria-hidden="true">&times;</span>' +
                    '</button></li>'
                    
        
       $('#ingredientsList').append(list_item + delete_btn);
   }
}

/**
 *Deletes selected item from list of ingredients
 */
function delete_ingredient(event, button) {  
    event.preventDefault();
    $(button).parent().remove();
}

/**
 *Forms row for table
 *@param {object} rowData This is a recipe that should be shown on the page  
 *@return {object} row This is a formed row
 */
function drawRow(rowData){
    var row = $('<tr />');
    row.append($('<td>' + rowData.name + '</td>'));
    row.append($('<td>' + rowData.ingredients.join(",") + '</td>'));
    row.append($('<td>' + rowData.time + '</td>'));
    row.append($('<td>' + rowData.recipe + '</td>'));
    
    return row;
}
