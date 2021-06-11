const postBtn = document.getElementById('ci-button');
// const getBtn = document.getElementById('ci-button');

const sendHttpRequest = (method,url) => {
    const promise = new Promise((resolve,reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method,url);
        xhr.onload = () =>{
            resolve(JSON.parse(xhr.response))
        }
        xhr.send();
    });
    return promise;
}

const sendData = () => {
    sendHttpRequest('POST','https://hkrsinvgen.herokuapp.com/api/post/'
    // ,{
    //     Billing_name : document.querySelectorAll("#cn"),
    //     Billing_Address : document.querySelectorAll("#ca"),
    //     Plan_Description : document.querySelectorAll("#pd"),
    //     Plan_Cost : document.querySelectorAll("#pc"),
    //     Quantity : document.querySelectorAll("#q"),
    //     Invoice_date : document.querySelectorAll("#ind"),
    //     Due_date: document.querySelectorAll("#dd"),
    //     Payment_mode : document.querySelectorAll("#pm"),
    //     Paid_date : document.querySelectorAll("#pda"),
    //     Paid_amt : document.querySelectorAll("#pa"),
    // }
    ).then(responseData => { 
        console.log(responseData);
        console.log(document.querySelectorAll("#pm"));
    });
};

// const getData = () => {
//     sendHttpRequest('GET','https://admin.aizotec.com/api/v1/version/').then(responseData => {
//         console.log(responseData)
//         for(obj_data in responseData){
//             console.log(responseData[obj_data].id ,responseData[obj_data].Version_no)
//         }
//     })
    
// };

postBtn.addEventListener('click',sendData)
// getBtn.addEventListener('click',getData)