import { Component, OnInit,EventEmitter,Output } from '@angular/core';
import {Events} from '../../models/eventModel';
import {DataService} from '../../services/data.service'

@Component({
  selector: 'app-icon',
  templateUrl: './icon.component.html',
  styleUrls: ['./icon.component.scss']
})
export class IconComponent implements OnInit {
  event:Events;

  colors=[
  "#e8eaed","#e6c9a8","#fdcfe8","#d7aefb","#f28b82","#fbbc04","#fff475","#ccff90","#a7ffeb",
    "#cbf0f8","#aecbfa","#d7aefb"
  ]
  note:any;
  @Output() eventCarrier = new EventEmitter<Events>();
  constructor(private dataService:DataService,) { }

  ngOnInit() {
  }

  colorElement(color){
    console.log("color",color)
    this.event={
      "purpose":"color",
      "value":color
    }
    console.log(this.note)
    this.eventCarrier.emit(this.event);

  }
}
