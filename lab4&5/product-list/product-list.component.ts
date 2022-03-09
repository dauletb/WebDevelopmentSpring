import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  num=0;
  bool:boolean=false;
  bool2:boolean=false;
  bool3:boolean=false;
  bool4:boolean=false;

  Switch1(){
    this.bool=!this.bool;
  }
  Switch2(){
    this.bool2=!this.bool2;
  }
  Switch3(){
    this.bool3=!this.bool3;
  }
  Switch4(){
    this.bool4=!this.bool4;
  }



  constructor() { }

  ngOnInit(): void {
  }

}
