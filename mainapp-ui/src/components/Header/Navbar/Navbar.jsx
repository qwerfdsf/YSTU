import React from 'react';
import NavbarItem from "./NavbarItem/NavbarItem";
import style from './Navbar.module.scss'

const Navbar = (props) => {
    let navbarItem = props.state.navbarItem.map( i => <NavbarItem src={i.src} item={i.item} link={i.link}/>)

    return (
        <div className={style.wrapper}>
            { navbarItem }
        </div>
    )
}

export default Navbar;