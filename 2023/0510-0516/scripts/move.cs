using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class spherePosition : MonoBehaviour
{
  void Start()
  {
    // 初期位置を設定する
    this.transform.position = new Vector3(0, 0, 0);
  }

  void Update()
  {
    if (Input.GetKey(KeyCode.A)) this.transform.position += new Vector3(0.1f, 0, 0);
    if (Input.GetKey(KeyCode.D)) this.transform.position += new Vector3(-0.1f, 0, 0);
    if (Input.GetKey(KeyCode.W)) this.transform.position += new Vector3(0, 0.1f, 0);
    if (Input.GetKey(KeyCode.S)) this.transform.position += new Vector3(0, -0.1f, 0);
  }
}