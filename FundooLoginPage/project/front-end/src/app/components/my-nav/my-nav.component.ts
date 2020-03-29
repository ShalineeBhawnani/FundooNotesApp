import { BreakpointObserver, Breakpoints, BreakpointState } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import {ChangeDetectorRef, Component, OnDestroy, OnInit} from '@angular/core';
import {MediaMatcher} from '@angular/cdk/layout';
import {Router} from '@angular/router'
import {Labels} from '../../models/labels';
import {LabelEditComponent} from '../label-edit/label-edit.component';
import {MatDialog} from '@angular/material/dialog';
import { DataService } from '../../services/data.service';
import { UserService } from '../../services/user.service';
import { ProfileComponent } from '../profile/profile.component';

@Component({
  selector: 'app-my-nav',
  templateUrl: './my-nav.component.html',
  styleUrls: ['./my-nav.component.scss']
})
export class MyNavComponent implements OnInit,OnDestroy{
  labels:Labels[];
  message:string;
  mobileQuery: MediaQueryList;
  profileImageUrl:any;
  private _mobileQueryListener: () => void;
  

  constructor(changeDetectorRef: ChangeDetectorRef, media: MediaMatcher,private routing:Router,private userService:UserService,private dataService:DataService, private dialog:MatDialog) {
    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListener = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addListener(this._mobileQueryListener);
    this.getLabels()
  }

  ngOnInit(){
     console.log("profile pic")
     this.getProfilemage();
  }

  // navigateTrash(){ 
  //   console.log("navigating to trash")
  //   this.routing.navigate(['nav/bin']);
  // }
  // navigateArchive(){
  //   this.routing.navigate(['nav/archive']);
  // }

  navigateToLabel(label){
  console.log(label);
    
    this.dataService.labelNext(label)
    this.routing.navigate(['/nav/label'+label])
  }
  
  getLabels(){
    console.log("getting labels",this.labels)
    this.userService.getAllLabel().subscribe(
      data => {
        this.labels = data;
        console.log("my data label",data)
      },
      
      error => {
        console.log(error);
      }
    );
  }
  openLabelEditBox(){
    console.log("inside dash open label func")
    let dialogref = this.dialog.open(LabelEditComponent,
      {
        
        data : {
          label:this.labels  
                
        }
        
      });
      console.log("label in nav",this.labels)
    dialogref.afterClosed().subscribe(result=> {
      //console.log("dialog result ", result);
      
    })
  }
 
  getProfilemage(){
    let profileImage=sessionStorage.getItem("fundooProfileimage");
   
    // this.profileImageUrl = `url(http://127.0.0.1:8000/${profileImage})`;
    this.profileImageUrl = profileImage
    console.log("put profile",this.profileImageUrl)
    

  }

  fileChangeEvent(event){
    const dialogRef = this.dialog.open(ProfileComponent, {
      width: 'auto',
      height:"auto",
      data: event
    });

    dialogRef.afterClosed().subscribe(result => {
      let fd=new FormData();
      fd.append('file',result);
      console.log(result);
      this.userService.uploadProfileImage(fd).subscribe((response:any)=>{
        sessionStorage.setItem("fundooProfileimage",response);
        this.getProfilemage();
      });
    });
  }
  ngOnDestroy(): void {
    this.mobileQuery.removeListener(this._mobileQueryListener);
  }
  
}
