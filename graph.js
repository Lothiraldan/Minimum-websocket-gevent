$(function() { 
    // Open up a connection to our server 
    var ws = new WebSocket("ws://localhost:10000/");

    // What do we do when we get a message? 
    ws.onmessage = function(evt) { 
        $("#placeholder").append('<p>' + evt.data + '</p>')
    } 
    // Just update our conn_status field with the connection status 
    ws.onopen = function(evt) { 
        $('#conn_status').html('<b>Connected</b>'); 
    } 
    ws.onerror = function(evt) { 
        $('#conn_status').html('<b>Error</b>'); 
    } 
    ws.onclose = function(evt) { 
        $('#conn_status').html('<b>Closed</b>'); 
    } 
}); 