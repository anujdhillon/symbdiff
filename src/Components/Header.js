import React, { Component } from 'react';
import {NavLink, Link} from 'react-router-dom';
class Header extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div className="Navbar">
                <nav className="nav">
                    <div className="logo">
                        <h1>Symbolic Differentiator</h1>
                    </div>
                    <div className="nav-items">
                        <div className="nav-item">
                            <NavLink to = "/" exact activeClassName="active">
                                Differentiator
                            </NavLink>
                        </div>
                        <div className="nav-item">
                            <NavLink to = "/instructions" exact activeClassName="active">
                                Instructions
                            </NavLink>
                        </div>        
                    </div>
                </nav>
            </div>
        )
    }
}
export default Header;