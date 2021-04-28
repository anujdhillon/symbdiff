import React, { Component } from 'react';
import Differentiator from './Differentiator';
import Instructions from './Instructions';
import {Switch, Route,withRouter} from 'react-router-dom';
class MainWindow extends Component{
    constructor(props){
        super(props);
        this.state = {
            fx: "",
            fprimex: "",
            loaded: true  
        }; 
        this.postData = this.postData.bind(this);
        this.getCookie = this.getCookie.bind(this);
    }
    
    getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    handleInputChange = (newInput) => {
        if(newInput === 'C'){
            this.setState({
                fx: this.state.fx.substring(0,this.state.fx.length-1)
            });   
        }
        else{
        this.setState({
            fx: this.state.fx.concat(newInput),
        });
        }
    };
    clear = () => {
        this.setState({
            fx: ""
        });
    };
    handleInputChangeFromKeyboard = (event) => {
        const target = event.target;
        const value = target.value;
        const name = target.name;
        this.setState({
                [name]: value
        });
    };
    async postData() {
        this.setState({
            loaded: false
        })
        var csrftoken = this.getCookie('csrftoken')
        const url = 'https://symbdiff.herokuapp.com/api/differentiate/';
        const response = await fetch(url,{
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken':csrftoken,
            },
            body: JSON.stringify({
                functiondata: this.state.fx
            })
        });  
        const data = await response.json();
        this.setState({
            fprimex: data.solution,
            loaded: true
        });
        
    };
    
    render(){
        return(
            <div className="MainWindow">
                <div className="content">
                <Switch>
                <Route path="/" exact>
                <Differentiator loading = {this.state.loading} fprimex = {this.state.fprimex} fx = {this.state.fx} handleInputChange={this.handleInputChange} handleInputChangeFromKeyboard = {this.handleInputChangeFromKeyboard} postData = {this.postData} clear = {this.clear}/>
                </Route>
                <Route path="/instructions" exact>
                  <Instructions/>
                </Route>  
                </Switch>
                </div>
            </div>
        );
    }
}
export default MainWindow;