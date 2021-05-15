import React from 'react';
import styles from './NavbarItem.module.scss'
import {NavLink} from "react-router-dom";

const NavbarItem = (props) => {
    return (
        <div className={styles.wrapper}>
            <NavLink to={props.link} className={styles.link}>
                <img className={styles.icon} src={props.src} alt=""/>
                {props.item}
            </NavLink>
        </div>
    )
}

export default NavbarItem;