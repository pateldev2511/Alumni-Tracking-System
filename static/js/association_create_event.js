// var event_name = "";
var event_file = "";
// var no_of_tickets_available = 0;
// var isEventFree = "";
// var ticket_price = "";
// var country_code = "";
// var start_date_time = "";
// var end_date_time = "";
// var event_description = "";
// var send_not_alumni = "";
// var send_not_colleges = "";
// var send_not_association = "";

function create_event()
{
    
    event_file = document.getElementById('event-file').value;
    if(event_file == "" || event_file.length == 0){
      document.getElementById('event-file').focus();
      Swal.fire({
        icon: 'error',
        title: 'Please Upload Event Poster / Image.',
      });
    }
    else{
        console.log("hello");
    }
}

// event-file
// event-name
// event-venue
// isTicketFree
// tickets-available
// ticket-price
// event-start-date-time
// event-end-date-time
// send_not_association
// send_not_colleges
// send_not_alumni


// session['c_event_name'] = ""
//                 session['c_tickets-available'] = ""
//                 session['c_ticket-price'] = ""
//                 session['c_event-start-date-time'] = ""
//                 session['c_event-end-date-time'] = ""
// session['c_event_description'] = ""
// // session['c_event_venue'] = ""
// session['s_not_association'] = send_not_association
//             session['s_not_colleges'] = send_not_colleges
//             session['s_not_alumni'] = send_not_alumni