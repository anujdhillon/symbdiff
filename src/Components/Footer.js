import React, { Component } from 'react';
import {faInstagram, faGithub, faYoutube} from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
class Footer extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return(
            <div className="Footer">
                <nav className="nav">
                    <div className="copyright">
                        <h4>@2021 Anuj Dhillon</h4>
                    </div>
                    <div className="icons">
                    <a href="https://github.com/anujdhillon/symbdiff" className="icon-holder">
                    <FontAwesomeIcon icon={faGithub} className="icon gh"/>
                    </a>
                </div>
                </nav>
            </div>
        )
    }
}
export default Footer;