$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(info) {
  $('DIV#hello').text(info.hello);
});