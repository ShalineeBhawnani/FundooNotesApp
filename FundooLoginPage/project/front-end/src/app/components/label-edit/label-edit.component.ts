import { Component, OnInit,Inject,Output,EventEmitter} from '@angular/core';
import { MAT_DIALOG_DATA, throwMatDuplicatedDrawerError } from '@angular/material';
import { FormControl, FormGroup, Validators}from '@angular/forms';
import { UserService } from '../../services/user.service';
import { DataService } from '../../services/data.service';
import {Events} from '../../models/eventModel'
import { MatSnackBar } from '@angular/material/snack-bar';
import {Labels} from '../../models/labels';
@Component({
  selector: 'app-label-edit',
  templateUrl: './label-edit.component.html',
  styleUrls: ['./label-edit.component.scss']
})
export class LabelEditComponent implements OnInit {
  labelName = new FormControl('', [
    Validators.required,

  ]);

  labels:Labels[];
  editingLabel:string;
  event:Events;
  notedata:any;
  labelid:any;
  constructor(@Inject(MAT_DIALOG_DATA) private data: any,private snackBar:MatSnackBar,private userService:UserService,private dataService:DataService) { }
  @Output() eventCarrier = new EventEmitter<Events>();
  ngOnInit() {
  }
  isBeingEdited(label){
    this.editingLabel=label.id;
  }
  isEditVisible(label){
    if(this.editingLabel==label.id)
    return true;
    else
    return false;
  }
updateLabel(label){
  
  this.notedata = {
     labeldata:label,
    "label":this.labelName.value,
  
  }
  this.labelid=this.notedata.labeldata.id
  console.log("label id data",this.labelid)
  this.userService.updateLabel(this.notedata,this.labelid).subscribe(
      (data) => {
        console.log("label id",this.labelid)
        this.snackBar.open(data.toString(),'',{
          duration:3000,
          verticalPosition:'bottom'
        });
          
      },
      error => {
        alert('Label updation failed')

      });
     
}

deleteLabel(label){
  
  this.data = {
    labeldata:label,
  }
  this.labelid=this.data.labeldata.id
  console.log("label id data",this.labelid)
  this.userService.deleteLabel(this.labelid).subscribe(
      (data) => {
        console.log("label id",this.labelid)
        this.snackBar.open(data.toString(),'',{
          duration:3000,
          verticalPosition:'bottom'
        });
          
      },
      error => {
        alert('Label updation failed')

      });
     
}

createLabel(){

    let data={
      label:this.labelName.value,
      isDeleted:false 
    }
    console.log("label add again",data)
    console.log("created label",data)
    this.userService.label(data).subscribe((data:any)=>{
   
    })
  }
}