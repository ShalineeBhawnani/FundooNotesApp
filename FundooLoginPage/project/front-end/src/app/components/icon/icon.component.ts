import { Component, OnInit,EventEmitter,Output } from '@angular/core';
import {Events} from '../../models/eventModel';
import {DataService} from '../../services/data.service';
import { UserService } from '../../services/user.service';
import {Labels} from '../../models/labels';
import { FormControl } from '@angular/forms';
import { MatDialog } from '@angular/material';



@Component({
  selector: 'app-icon',
  templateUrl: './icon.component.html',
  styleUrls: ['./icon.component.scss']
})
export class IconComponent implements OnInit {
  event:Events;
  labelIdList:string[];
  colors=[
  "#e8eaed","#e6c9a8","#fdcfe8","#d7aefb","#f28b82","#fbbc04","#fff475","#ccff90","#a7ffeb",
    "#cbf0f8","#aecbfa","#d7aefb"
  ]
  newLabel:string;
  label:Labels[];
  save:Boolean=false;
  message:string;
  note:any;
  labelCheck = new FormControl();
  dummy:boolean=false;
  @Output() eventCarrier = new EventEmitter<Events>();
  @Output() saveNotes = new EventEmitter<Boolean>();

  constructor(private dataService:DataService,private userSerive:UserService) { }

  ngOnInit() {
    this.dataService.currentMessage.subscribe(message => this.message = message)
    this.getLabels();
    
  }
  
  saveNote() {
    this.save=true;
    this.saveNotes.emit(this.save);
  }
  archive(){
    this.event={
      "purpose":"archive",
    }
   
    this.eventCarrier.emit(this.event);
  }
  deleteNotes(){
    this.event={
      "purpose":"deleteNote",
    }
    this.eventCarrier.emit(this.event);
  }
  getLabels(){
    console.log("getting labels",this.label)
    this.userSerive.getAllLabel().subscribe(
      data => {
       
        this.label = data;
        console.log("my data label",data)
      },
      
      error => {
        console.log(error);
      }
    );
  }
  
  
  // addLabel(){
  //   //console.log("in add lable")
  //   let data={
  //     "label":this.newLabel,
  //     "userId":localStorage.getItem('userId'),
  //     "isDeleted":false 
  //   }
  //   this.userSerive.addLabel(data).subscribe((data:any)=>{
  //     this.getLabels();
  //     this.newLabel="";
 

  //   })

    
  //   //console.log(this.labels)
  // }


 
  // labelAddOrRemove(label){
  //   let data={
  //     "noteId":this.noteId,
  //     "label":label
  //   }
  //   this.event={
  //     "purpose":"addLabel",
  //     "value":data
  //   }
   
  //   this.eventCarrier.emit(this.event);
  // }


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
