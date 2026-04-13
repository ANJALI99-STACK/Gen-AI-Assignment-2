$(document).ready(function(){

const responses = [
    "That’s interesting!",
    "Tell me more 👀",
    "I can help with that!",
    "Nice question!",
    "Let’s explore that."
];

// Add message
function addMessage(text, sender){
    const time = new Date().toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'});

    let msg = `
    <div class="message ${sender}">
        <div>${text}</div>
        <small>${time}</small>
    </div>`;

    $("#messages").append(msg);
    scrollBottom();
}

// Scroll
function scrollBottom(){
    $("#messages").scrollTop($("#messages")[0].scrollHeight);
}

// Send
function sendMessage(){
    let text = $("#input").val().trim();
    if(!text) return;

    addMessage(text,"user");
    $("#input").val("").css("height","auto");
    $("#sendBtn").prop("disabled", true);

    $("#welcome").hide();
    $("#typing").show();

    setTimeout(()=>{
        $("#typing").hide();
        let reply = responses[Math.floor(Math.random()*responses.length)];
        addMessage(reply,"ai");
    },1500);
}

// Click send
$("#sendBtn").click(sendMessage);

// Enable/disable button
$("#input").on("input", function(){
    $("#sendBtn").prop("disabled", !this.value.trim());

    // Auto resize
    this.style.height = "auto";
    this.style.height = this.scrollHeight + "px";
});

// Enter key
$("#input").keydown(function(e){
    if(e.key === "Enter" && !e.shiftKey){
        e.preventDefault();
        sendMessage();
    }
});

// Sidebar toggle
$("#menuBtn").click(function(){
    $("#sidebar").addClass("active");
    $("#overlay").addClass("active");
});

$("#overlay").click(function(){
    $("#sidebar").removeClass("active");
    $("#overlay").removeClass("active");
});

// New chat
$(".new-chat").click(function(){
    $("#messages").empty();
    $("#welcome").show();
});

});