import { Component } from '@angular/core';
import {faCartPlus} from '@fortawesome/free-solid-svg-icons';
import {faStar} from '@fortawesome/free-solid-svg-icons';
import {faStarHalf} from '@fortawesome/free-solid-svg-icons';
import { faHome } from '@fortawesome/free-solid-svg-icons';
import { faBook } from '@fortawesome/free-solid-svg-icons';
import { faFolder } from '@fortawesome/free-solid-svg-icons';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  ic=faCartPlus;
  full=faStar;
  text="hello";
  half=faStarHalf;
  home=faHome;
  book=faBook;
  phone=faFolder;
  title = 'my-app';
  num="a";
  
  products: any[];
  constructor(){
    this.products=[{"name":"65w USB c","description":"PDUSBSZ 65W USB C Power Adapter, Type C Power PD Wall Fast Charger Compatible with Mac Book Pro, Dell Latitude, Lenovo, Huawei Matebook, HP Spectre, Acer Chromebook and Any Laptops or Smart Phones",image:["i1.jfif","i2.jfif"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"name":"Logitech C920x HD","description":"-",image:["b1.jfif","b2.jfif"],rat:[this.full,this.full,this.full]},
    {"name":"ApplePencil 1 gen","description":"-",image:["c1.jfif"],rat:[this.full,this.full,this.full]},
    {"name":"Logitech MK270 keyboard wireless","description":"--",image:["d1.jfif","d2.jfif"],rat:[this.full,this.full,this.full]},
    {"name":"Air Pods 2Generation","description":"--",image:["e1.jfif","e2.jfif"],rat:[this.full,this.full,this.full]},
    {"name":"fitbit sense advanced smartwatch","description":"--",image:["f1.jfif","f2.jfif"],rat:[this.full,this.full,this.full]},
    {"name":"wyze cam3","description":"--",image:["g1.jfif","g2.jfif","g3.jfif"],rat:[this.full,this.full,this.full]},
    {"name":"logitech h390, black","description":"--",image:["h1.jfif","h2.jfif","h3.jfif"],rat:[this.full,this.full,this.full]},
    {"name":"MI-84 graphing calculator, Texas Instruments","description":"--",image:["a1.jfif","a2.jfif"],rat:[this.full,this.full,this.full]},
    {"name":"matein travel laptop backpack","description":"--",image:["j1.jfif","j2.jfif"],rat:[this.full,this.full,this.full]},
    {"name":"HyperX- Quadcast","description":"--",image:["k1.jfif","k2.jfif"],rat:[this.full,this.full,this.full]}
    ]
  }

}
