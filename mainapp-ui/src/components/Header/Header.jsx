import React from 'react';
import styles from './Header.module.scss'
import MainHeader from "./MainHeader/MainHeader";
import Navbar from "./Navbar/Navbar";

const Header = (props) => {
    return (
        <div className={styles.header}>
            <div className={styles.wrapper}>
                <MainHeader/>
                <Navbar state={props.state.header}/>
            </div>

        </div>
    )
}

export default Header;