// TODO get form elements from the page
console.log("hello")

const baseUrl = "http://127.0.0.1:5000/"

// *get values from the form
$("cupcake-form").on("submit", async function () {
    let flavor = $("flavor-input").val()
    let rating = $("rating-input").val()
    let size = $("size-input").val()
    let image = $("image-input").val()
    // *async request **** match the route as it is set on the backend **** pass in the params from the form as the post
    const resp = await axios.post('${baseUrl}'/cupcakes, {
        flavor,
        rating, 
        size,
        image
    })


})