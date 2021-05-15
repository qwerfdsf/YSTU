import React from 'react';
import {BrowserRouter, Route} from "react-router-dom";
import './App.css';
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import Profile from "./components/Profile/Profile";
import Portfolio from "./components/Portfolio/Portfolio";
import Events from "./components/Events/Events";
import Vacancies from "./components/Vacancies/Vacancies";


const App = (props) => {
    return (
        <BrowserRouter>
            <div>
                <Header state={props.state}/>
                <div className="content">
                    <Route path='/profile'>
                        <Profile/>
                    </Route>
                    <Route path='/portfolio'>
                        <Portfolio/>
                    </Route>
                    <Route path='/events'>
                        <Events/>
                    </Route>
                    <Route path='/vacancies'>
                        <Vacancies/>
                    </Route>
                </div>
                <Footer/>
            </div>
        </BrowserRouter>
    )
}

export default App;
