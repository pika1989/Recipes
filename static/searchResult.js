$(document).ready(function() {
  $('#btn_search').click(function() {
    search_by_ingredient();
    return false;
  });

  $('#btn_add').click(function() {
    add_ingredient();
    return false;
  });
});

function search_by_ingredient() {

  var post_data = {};
  $("li").map(function(id) {
    post_data['ingredient'+id] = $(this).text();
  });

  $.post('/search', post_data)
    .done(function(data) {
    $('#dishTable tbody').empty();
    var dishes = JSON.parse(data);
    for(var i = 0; i < dishes.length; i++){
       $('tbody').append(drawRow(dishes[i]));
    }
  });
}

function add_ingredient() {
   var ingredient = $('#ingredient').val();
   var ingr_array = [];
   ingr_array.push(ingredient);
   $('#ingredientsList').append('<li><h4>'+ ingredient + '</h4></li>');
}

function drawRow(rowData){
    var row = $('<tr />');
    row.append($('<td>' + rowData.name + '</td>'));
    row.append($('<td>' + rowData.ingredients.join(",") + '</td>'));
    row.append($('<td>' + rowData.time + '</td>'));
    row.append($('<td>' + rowData.recipe + '</td>'));
    
    return row;
}
