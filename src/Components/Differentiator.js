import React, { Component } from 'react';
import buttons from './buttons';
class Differentiator extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div className="inputarea">
                <div className="buttonarea">
                    {
                        buttons.map((button) =>{
                            return <button onClick = {() => {this.props.handleInputChange(button.label)}}  className={`btn ${button.type}`}>{button.label}</button>
                        })
                    }
                </div>
                <div className="submitarea">
                    <div className="inputtext">
                        <textarea type="text" id="fx" name="fx" placeholder="Type Here" value = {this.props.fx} onChange={this.props.handleInputChangeFromKeyboard}/>
                    </div>
                    <div className="handlebuttons">
                        <button onClick={ () => this.props.postData() } className="btn diff">Differentiate</button>
                        <button onClick={ () => this.props.clear()} className="btn clear">Clear</button>
                    </div>
                    <div className="outputtext">
                        <textarea readOnly type="text" id="fprimex" name="fprimex" placeholder="Solution" value = {this.props.loading?"Finding":this.props.fprimex}/>
                    </div>
                </div>
            </div>
        )
    }
}
export default Differentiator;