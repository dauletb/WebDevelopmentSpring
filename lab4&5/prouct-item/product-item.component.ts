import { Component, OnInit } from '@angular/core';
import {faCartPlus} from '@fortawesome/free-solid-svg-icons';
import {faStar} from '@fortawesome/free-solid-svg-icons';
import {faStarHalf} from '@fortawesome/free-solid-svg-icons';
import { faHeart } from '@fortawesome/free-solid-svg-icons';
import { Input } from '@angular/core';
import { faCircleMinus } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  ic=faCartPlus;
  full=faStar;
  half=faStarHalf;
  heart=faHeart;
  title = 'my-app';
  num="a";
  rem=faCircleMinus;
  @Input()
  arr!: any[];

  products: any[];
  constructor(){
    this.products=[{"exists":true,"likes":0,"name":"65w USB c","description":"PDUSBSZ 65W USB C Power Adapter, Type C Power PD Wall Fast Charger Compatible with Mac Book Pro, Dell Latitude, Lenovo, Huawei Matebook, HP Spectre, Acer Chromebook and Any Laptops or Smart Phones",image:["i1.jfif","i2.jfif"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"Logitech C920x HD","description":"Logitech HD Pro Webcam C920, Widescreen Video Calling and Recording, 1080p Camera, Desktop or Laptop Webcam Price:	$62.95",image:["b1.jfif","b2.jfif"],rat:[this.full,this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"ApplePencil 1 gen","description":"With Apple Pencil, you can turn iPad into your notepad, canvas, or just about anything else you can imagine.(Not in sale)",image:["c1.jfif"],rat:[this.full,this.full,this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"Logitech MK270 keyboard wireless","description":"Logitech MK270 Wireless Keyboard and Mouse Combo for Windows, 2.4 GHz Wireless, Compact Mouse, 8 Multimedia and Shortcut Keys, 2-Year Battery Life, for PC, Laptop price $23.95",image:["d1.jfif","d2.jfif"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"Air Pods 2Generation","description":"Effortless setup, in-ear detection, and automatic switching for a magical experience(Not in sale",image:["e1.jfif","e2.jfif"],rat:[this.full,this.full,this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"fitbit sense advanced smartwatch","description":"Fitbit Sense Advanced Smartwatch with Tools for Heart Health, Stress Management & Skin Temperature Trends, Carbon/Graphite, One Size (S & L Bands Included) Price:	$224.00 ($224.00 / Count)",image:["f1.jfif","f2.jfif"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"wyze cam3","description":"Wyze Cam v3 with Color Night Vision, Wired 1080p HD Indoor/Outdoor Video Camera, 2-Way Audio, Works with Alexa, Google Assistant, and IFTTT (Temporarily out of stock)",image:["g1.jfif","g2.jfif","g3.jfif"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"logitech h390, black","description":"Logitech H390 Wired Headset, Stereo Headphones with Noise-Cancelling Microphone, USB, In-Line Controls, PC/Mac/Laptop - Black 29.00$",image:["h1.jfif","h2.jfif","h3.jfif"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"MI-84 graphing calculator, Texas Instruments","description":"--",image:["a1.jfif","a2.jfif"],rat:[this.full,this.full,this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"matein travel laptop backpack","description":"Texas Instruments TI-84 Plus CE Color Graphing Calculator, Black 7.5 Inch Price:	$124.05",image:["j1.jfif","j2.jfif"],rat:[this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"HyperX- Quadcast","description":"HyperX QuadCast - USB Condenser Gaming Microphone, for PC, PS4, PS5 and Mac, Anti-Vibration Shock Mount, Four Polar Patterns, Pop Filter, Gain Control, Podcasts, Twitch, YouTube, Discord, Red LED Price:	$89.99",image:["k1.jfif","k2.jfif"],rat:[this.full,this.full,this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"TI-30 IIS Calculator","description":"Texas Instruments TI-30XIIS Scientific Calculator, Black with Blue Accents Price:	$12.97",image:["ti-30.jfif","ti-30(2).jfif"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"Oasis Kindle","description":"Kindle Oasis Essentials Bundle including Kindle Oasis (Graphite, Ad-Supported), Amazon Leather Cover, and Power Adapter Bundle Price:	$319.97",image:["oasis.jfif","oasis(2).jfif"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"Nbada Office Chaair","description":"Hbada Ergonomic Office Recliner Chair - High-Back Desk Chair Racing Style with Lumbar Support - Height Adjustable Seat, Headrest- Breathable Mesh Back - Soft Foam Seat Cushion with Footrest, Black Price:	$199.99",image:["hbada.jfif","hbada2.jfif"],rat:[this.full,this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"Blink Outdoor Camera","description":"Blink Outdoor - wireless, weather-resistant HD security camera, two-year battery life, motion detection, set up in minutes – 2 camera kit (Temporarily out of stock)",image:["blink.jfif","blink22.jfif"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"ISO48 camera","description":"Polaroid IS048 Waterproof Instant Sharing 16 MP Digital Portable Handheld Action Camera, Teal price:35.00$",image:["iso48.jfif"],rat:[this.full,this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"Empsign18 Backpack for school","description":"--",image:["empsign18.jpg"],rat:[this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"lovevook Backpack for school","description":"LOVEVOOK Quilted Laptop Backpack Stylish Laptop Bag for Women Work Computer Bags Bookbag Purse,15.6-Inch, Black (Currently Unavailable)",image:["lovevook.jpg"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"ugrace backpack for school with charger","description":"UGRACE Vintage Laptop Backpack with USB Charging Port, Elegant Water Resistant Travelling Backpack Casual Daypacks School Shoulder Bag for Men Women, Fits up to 15.6Inch Laptop in Green. With Deal:	$25.49",image:["ugrace.jpg"],rat:[this.full,this.full,this.full,this.full,this.half]},
    {"exists":true,"likes":0,"name":"Ikunst bag","description":"iKunst Laptop Backpack for Women Men, 15.6 Inch Stylish Anti-Theft Casual Travel College School Backpack Business Computer Bookbag with USB Charging Port, Black Price:	$29.99",image:["ikunst.jpg"],rat:[this.full,this.full,this.full,this.full]},
    {"exists":true,"likes":0,"name":"yootech charger","description":"Yootech Wireless Charger,Qi-Certified 10W Max Fast Wireless Charging Pad Compatible with iPhone 13/13 Pro/13 Mini/13 Pro Max/12/SE 2020/11,Samsung Galaxy S22/S21/S20/S10,AirPods Pro(No AC Adapter) Price:	$12.99",image:["yootech.jfif","yootech2.jfif","yootech3.jfif"],rat:[this.full,this.full,this.full,this.full,this.half]}
    ]
  }



  ngOnInit(): void {
  }

}
