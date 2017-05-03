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
    console.log(data);
  });
}

function add_ingredient() {
   var ingredient = $('#ingredient').val();
   var ingr_array = [];
   ingr_array.push(ingredient);
   $('#ingredientsList').append('<li><h4>'+ ingredient + '</h4></li>');
}


