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

  $('#ingredientsList').click(function( event ) {
    var target = $( event.target );
    if ( target.is( "li" ) ) {
      alert( target.index() );
    return false;
    }
  });
});


/**
 * Gets list of ingredients from form, sends request data
 * to backend, gets results and shows them in table
 */
function search_by_ingredient() {

  var post_data = {};
  $("li").map(function(id) {
    post_data['ingredient'+id] = $(this).text();
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
   var ingr_array = [];
   ingr_array.push(ingredient);
   $('#ingredientsList').append('<li>'+ ingredient + '</li>');
}

/**
 *Deletes selected item from list of ingredients
 */
function delete_ingredient(ingredient) {  
    alert(ingredient + "is clicked")
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
