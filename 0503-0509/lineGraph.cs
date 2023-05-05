using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class lineGraph : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // CSVファイルのパスを設定する
        string filePath = Application.dataPath + "/data.csv";

        // CSVファイルを開く
        StreamReader reader = new StreamReader(filePath);

        // データを読み込む
        List<Vector3> points = new List<Vector3>();
        while (!reader.EndOfStream)
        {
            string[] line = reader.ReadLine().Split(',');
            float x = float.Parse(line[0], System.Globalization.NumberStyles.Float);
            float y = float.Parse(line[1], System.Globalization.NumberStyles.Float);
            float z = float.Parse(line[2], System.Globalization.NumberStyles.Float);
            points.Add(new Vector3(x, z, y));
        }

        // ファイルを閉じる
        reader.Close();

        // LineRendererコンポーネントをアタッチする
        LineRenderer lineRenderer = gameObject.AddComponent<LineRenderer>();

        // 線の幅を設定する
        lineRenderer.startWidth = 0.1f;
        lineRenderer.endWidth = 0.1f;

        // 点の数を設定する
        lineRenderer.positionCount = points.Count;

        // 点の座標を設定する
        for (int i = 0; i < points.Count; i++)
        {
            lineRenderer.SetPosition(i, points[i]);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
