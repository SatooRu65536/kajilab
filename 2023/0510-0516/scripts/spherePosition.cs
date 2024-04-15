using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class spherePosition : MonoBehaviour
{
    public string filePath = Application.dataPath + "/point.csv";
    public float scale = 1;  // 球の大きさの倍率

    private List<Vector3> positions = new List<Vector3>();  // データを格納するリスト
    private List<float> times = new List<float>();
    private int currentIndex = 0;  // 現在のインデックス
    private float timer = 0;  // タイマー

    void Start() {
        StreamReader reader = new StreamReader(filePath);
        reader.ReadLine();

        while (!reader.EndOfStream) {
            string[] line = reader.ReadLine().Split(',');
            float x = float.Parse(line[1]);
            float y = float.Parse(line[2]);
            float z = float.Parse(line[3]);
            positions.Add(new Vector3(x, z, y));
            times.Add(float.Parse(line[0]));
        }

        this.transform.position = new Vector3(0, 0, 0);
    }

    void Update() {
        // アニメーションを実行する
        timer += Time.deltaTime * 4;

        float diff_time;
        if (currentIndex == 0) diff_time = 0;
        else diff_time = times[currentIndex] - times[currentIndex - 1];

        if (timer >= diff_time) {
            currentIndex++;
            if (currentIndex >= positions.Count) currentIndex = 0;

            transform.position = positions[currentIndex];
            timer = 0;
        }
    }
}