// function gettypevalue(){
//       var uitype = document.getElementById("uitype");
//       for(var i in uitype){
//         if(uitype[i].checked) {
//             return parseInt(i)+1;
//         }
//       }
//       return -1; //invalid value
// }
// function getage_groupvalue(){
//     var uiage_group = document.getElementById("uiage_group");
//     for(var i in uiage_group){
//       if(uiage_group[i].checked) {
//           return parseInt(i)+1;

//       }
//     }
//     return -1; //invalid value

// }
// function getgendervalue(){
//     var uigender = document.getElementById("uigender");
//     for(var i in uigender){
//       if(uigender[i].checked) {
//           return parseInt(i)+1;
//       }
//     }
//     return -1; //invalid value

// }


function onClickEstimateRate() {
    const data = {
        Year: document.getElementById("uiyear").value,
        Type: document.getElementById("uitype").value,
        Age_group: document.getElementById("uiage_group").value,
        Gender: document.getElementById("uigender").value,
        State: document.getElementById("uistate").value,
    }

    console.log(data)

    var estRate = document.getElementById("uiEstimateRate");

    var url = "http://127.0.0.1:5000/predict_suicide_rate";

    $.post(url, {
        ...data
    }, function (data, status) {
        estRate.innerHTML = "<h2>" + data.estimated_suicide + "Lakh</h2>";
    });
}



function onPageLoad() {
    var url = "http://127.0.0.1:5000/get_state_names";
    $.get(url, function (data, status) {
        if (data) {
            var state = data.state;
            var uistate = document.getElementById("uistate");
            $('#uistate').empty();
            for (var i in state) {
                var opt = new Option(state[i], i);
                $('#uistate').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;