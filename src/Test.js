import React from "react";
import axios from "axios";
import api from "./service"

class Test extends React.Component{

       
    componentDidMount(){

        api.get("about").then((res)=>{
            console.log('res.data', res)
        })


    }

    render(){
        return(
            <div> HEllo</div>

        )
    }

}

export default Test;