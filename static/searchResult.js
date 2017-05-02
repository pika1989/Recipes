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
  var post_data = {}
  post_data['ingredient'] = $('#ingredient').val();
  var ingr_array = [];
  ingr_array.push($('#ingr1').val());
  $.post('/search', post_data)
    .done(function(data) {
    console.log(data);
  });
}

function add_ingredient() {
   var ingredient = $('#ingredient').val();
   var ingr_array = [];
   ingr_array.push(ingredient);
   $('#ingredientsList').append('<li><h3>' + ingredient + '</h3></li>');
}


