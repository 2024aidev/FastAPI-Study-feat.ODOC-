// $.getJSON('http://127.0.0.1:5000/echo_call/[13,201230,202176933,20359,201,205,2019,208,202]', function(data) {
//     console.log(data);
//     document.getElementById("demo").innerHTML = data['output_data'];
// });
// $.getJSON('http://127.0.0.1:5000/echo_call/[0,100,200,0,0,0,0,0,0]', function(data) {
//     console.log(data);
//     document.getElementById("demo").innerHTML = data['add_result'];
// });


// $.getJSON('http://192.168.0.21:8000/add/1/2', function(data) {
//     console.log(data);
//     document.getElementById("demo").innerHTML = data['add result'];
// });



fetch("http://127.0.0.1:8000/add/1/2").then((Response) => {
    return Response.json()
}).then((data) => {
    console.log(data);
    document.getElementById("demo").innerHTML = data['add'];
})


fetch("http://127.0.0.1:8000/sub/3/1").then((Response) => {
    return Response.json()
}).then((data) => {
    console.log(data);
    document.getElementById("demo2").innerHTML = data['sub'];
})
    


