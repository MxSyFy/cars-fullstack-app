// /pages/CarModels.jsx

import { useState, useEffect, useRef } from "react";

export default function CarModels() {
    const [carModelData, setCarModelData] = useState([]); 
    const [newCarModel, setNewCarModel] = useState({});
    const [responseStatus, setResponseStatus] = useState(null);

    const formRef = useRef(null);

    const fetchData = async () => {
        const apiData = await fetch(`http://127.0.0.1:8000/api/v1/carmodels/`);
        const apiJSON = await apiData.json();
        setCarModelData(apiJSON.result);
    };

    useEffect(() => {
        fetchData();
    }, []);

    const addNewCarModel = async (carModel) => {
        const response = await fetch(`http://127.0.0.1:8000/api/v1/carmodels/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(carModel),
        });
        return response;
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData(formRef.current);

        const carModel = {
            make: formData.get("make"),
            model: formData.get("model")
        };

        const response = await addNewCarModel(carModel);
        if (response.ok) {
            setResponseStatus(200);
            formRef.current.reset();
            fetchData();
        } else {
            setResponseStatus(response.status);
        }
    };

    return (
        <div>
            <h1>Car Models</h1>
            <ul>
                {carModelData.map(carModel => (
                    <li key={carModel.car_model_id}>
                        <h3>Car Model ID: {carModel.car_model_id} - {carModel.make} - {carModel.model}</h3>
                    </li>
                ))}
            </ul>
            <h2>Add a Car Model Below:</h2>
            <form ref={formRef} onSubmit={handleSubmit}>
                <h5>Make:</h5><input name="make" type="text" required></input>
                <h5>Model:</h5><input name="model" type="text" required></input>
                <button type="submit">Add a new car model</button>
            </form>
            {responseStatus === 200 && <h3>Successfully added {newCarModel.make} - {newCarModel.model}</h3>}
            {responseStatus && responseStatus !== 200 && <h3>Failed to add new car model (Status: {responseStatus})</h3>}
        </div>
    );
}



// import { useState, useEffect, useRef } from "react";

// export default function Cars() {

//     const [carData, setCarData] = useState([]) 
//     const [newCar, setNewCar] = useState({})
//     const [response, setResponse] = useState()

//     const formRef = useRef(null);

//         const fetchData = async () => {
          
//           const apiData = await fetch(`http://127.0.0.1:8000/api/v1/cars/all_car_models`);
//           const apiJSON = await apiData.json();
//           setCarData(apiJSON)
//         };

//         useEffect(() => {
//             fetchData()
//            }, []) 


//         //Post a new car api call
//        const addNewCar = async () => {
//         const response = await fetch(`http://127.0.0.1:8000/api/v1/cars/all_car_models`, {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify(newCar),
//     })

    
//    return response }
    
//        const handleSubmit = async (event) => {
//         event.preventDefault();
//         const formData = new FormData(formRef.current);  
 
//         const car = {
//             make: formData.get("make"),
//             model: formData.get("model")
//         } 
//         setNewCar(car)
//         const response = await addNewCar(car);
//     if (response.ok === true) {
//         console.log("response ok")
//         formRef.current.reset();
//         fetchData();
//     }
//     }



//     useEffect(() => {
//         const addNewCarAsync = async () => {
//             // Submit the new car data
//             const response = await addNewCar(newCar);
//             setResponse(response)
//             console.log(response)
            
//         };
        
    
//         if (newCar.make && newCar.model) {
//             addNewCarAsync();
//         }
//     }, [newCar]);
        
       
       
       
  
    


//     return (
//         <div>
//             <h1>Cars</h1>
//             <ul>
//                     {carData.map(car => (
//                         <li key={car.pk}>
//                             <h3>Car ID: {car.pk} - {car.fields.make} - {car.fields.model}</h3>
//                         </li>
//                     ))}
                
//             </ul>
//             <h2>Add a Car Below:</h2>
//             <form ref={formRef} onSubmit={handleSubmit}>
//             <h5>Make:</h5><input name="make" type="text"></input>           
//             <h5>Model:</h5><input name="model" type="text"></input>
            
//             <button type="submit" >Add a new car</button>
//             </form>
//             {response === 200 && <h3>successfully added {newCar.pk} - {newCar.make} - {newCar.model}</h3>}
//         </div>
//     )
// }